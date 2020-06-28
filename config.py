settings = dict()
settings['images_list'] = '/images_list.yml'
settings['images_dir'] = '/put_cleaned'
settings['batch_size'] = 2
settings['nb_epoch'] = 1
settings['device'] = 'cuda'
settings['generator_path'] = 'model/model_generator_{}.pth'
settings['discriminator_path'] = 'model/model_discriminator_{}.pth'
settings['opt_G_path'] = 'opt/opt_generator_{}.pth'
settings['opt_D_path'] = 'opt/opt_discriminator_{}.pth'
settings['histo'] = 'pickle'
settings['light_cnn'] = 'LightCNN_29Layers_V2_checkpoint.pth.tar'