epoch = 0
iteration = 10
losses = [2.44161]

total = 164646
eta_str = 1864648
elapsed = 46464864
loss_labels = [6456, 456]

print(('[%3d] %7d ||' + (' %s: %.3f |' * len(losses)) + ' T: %.3f || ETA: %s || timer: %.3f')
      % tuple([epoch, iteration] + loss_labels + [total, eta_str, elapsed]), flush=True)