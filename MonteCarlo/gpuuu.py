import objc
from Cocoa import *
from Metal import *

# Configura un oggetto MTLDevice (che rappresenta la GPU)
device = MTLCreateSystemDefaultDevice()

# Verifica se il dispositivo Metal è supportato
if device is None:
    raise Exception("Metal non è supportato sul tuo dispositivo.")

# Crea una command queue
command_queue = device.newCommandQueue()

# Crea un array di numeri (ad esempio, 10,000 valori)
n = 10000
data = [i for i in range(n)]  # Dati da elaborare
data_length = len(data) * 4  # Ogni int occupa 4 byte (32 bit)

# Crea un buffer per i dati di input
input_buffer = device.newBufferWithBytes_length_options_(data, data_length, MTLResourceStorageModeShared)

# Crea un buffer per i risultati
output_buffer = device.newBufferWithLength_options_(data_length, MTLResourceStorageModeShared)

# Crea uno shader Metal (kernel) che quadratica i numeri
shader_code = """
#include <metal_stdlib>
using namespace metal;

kernel void square_numbers(const device int* in_data [[buffer(0)]],
                            device int* out_data [[buffer(1)]],
                            uint id [[thread_position_in_grid]]) {
    out_data[id] = in_data[id] * in_data[id];
}
"""

# Compilazione dello shader
library = device.newLibraryWithSource_options_error_(shader_code, None, None)
function = library.newFunctionWithName_("square_numbers")
pipeline = device.newComputePipelineStateWithFunction_error_(function, None)

# Crea una command encoder
command_buffer = command_queue.commandBuffer()
compute_encoder = command_buffer.computeCommandEncoder()

# Imposta il pipeline e i buffer di input e output
compute_encoder.setComputePipelineState_(pipeline)
compute_encoder.setBuffer_offset_atIndex_(input_buffer, 0, 0)
compute_encoder.setBuffer_offset_atIndex_(output_buffer, 0, 1)

# Imposta la griglia di esecuzione
threads_per_group = 256
threadgroups = (n + threads_per_group - 1) // threads_per_group  # Calcola il numero di threadgroups necessari
compute_encoder.dispatchThreadgroups_threadsPerThreadgroup_((threadgroups, 1, 1), (threads_per_group, 1, 1))

# Esegui il comando
compute_encoder.endEncoding()
command_buffer.commit()
command_buffer.waitUntilCompleted()

# Recupera i risultati dal buffer
out_data = objc.NULL
out_data = output_buffer.contents()

# Stampa i primi 10 risultati
print("Primi 10 numeri quadrati calcolati sulla GPU:")
for i in range(10):
    print(out_data[i])q