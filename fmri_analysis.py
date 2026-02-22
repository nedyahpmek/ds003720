from nilearn import plotting, image
import nibabel as nib
import numpy as np

fmri_path = "C:\Users\hayden\Documents\GitHub\ds003720\sub-001\func\sub-001_task-Test_run-01_bold.nii"
fmri_img = nib.load(fmri_path)

print(fmri_img.shape)

mean_fmri = image.mean_img(fmri_img)

plotting.plot_stat_map(
    mean_fmri,
    title="Mean fMRI Activation",
    display_mode="ortho",
    threshold=1.5
)

plotting.show()

smoothed = image.smooth_img(mean_fmri, fwhm=6)

plotting.plot_stat_map(
    smoothed,
    title="Smoothed Mean fMRI Activation",
    display_mode="ortho"
)

plotting.show()