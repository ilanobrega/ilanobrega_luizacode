import time

def esquentar_agua():
    return "Agua quente"

def colocar_po():
    return "Coloquei pó"

def coar():
    return "Cafe coado"

def fazer_cafe():
    start = time.time()
    
    esquentar_agua()
    time.sleep(1000) #para o tempo
    
    colocar_po()
    coar()
    time.sleep(500) 
    
    end = time.time()
    
    calculo_tempo = end - start
    return f'Cafe servido {calculo_tempo}'

print(fazer_cafe())