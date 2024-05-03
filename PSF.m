clearvars, close all

% Define image size
imageSize = 101;

% Create randomly distributed delta functions as ideal point sources
npts = 10; % number of points
delta = zeros(imageSize, imageSize);
for i = 1:npts
    delta(randi([1 imageSize],1,1), randi([1 imageSize],1,1)) = 1;
end

% Define a simple Gaussian blur PSF
sigma = 5; % Adjust sigma for different blur levels
psf = fspecial('gaussian', imageSize, sigma);

% Simulate the blurred image by convolving the point source with the PSF
blurredImage = conv2(delta, psf, 'same');

% Plot the ideal point source, PSF, and blurred image
figure;

% Plot the ideal point sources (delta functions)
subplot(1,3,1);
imagesc(delta);
title('Ideal Point Sources');
axis image
axis off

% Plot the PSF
subplot(1,3,2);
imagesc(psf);
title('Point Spread Function (PSF)');
axis image
axis off

% Plot the blurred image
subplot(1,3,3);
imagesc(blurredImage);
title('Blurred Image');
axis image
axis off

% Adjust layout and titles 
sgtitle('PSF Visualization');