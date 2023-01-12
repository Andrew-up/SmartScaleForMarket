from tensorflow import config


def setLimitGPU(memorySizeMB):

    try:
        gpus = config.experimental.list_physical_devices('GPU')  # Получить список GPU
        if gpus is not None:
            print('Используется GPU')
            config.experimental.set_virtual_device_configuration(gpus[0], [
                config.experimental.VirtualDeviceConfiguration(memory_limit=memorySizeMB)])
    except Exception:
        print('Нет GPU')
    # Первый параметр - это принцип, какой GPU, только один - gpu [0], memory_limt позади - это ограниченный размер видеопамяти, единица - M
