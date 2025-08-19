# CT Radon Transform & Filtered Back-Projection (FBP) Demo

This repo demonstrates the full toy pipeline used in computed tomography (CT):

1. Create a **Shepp–Logan phantom** (ground-truth object).
2. Compute its **Radon transform** to get a **sinogram** (line integrals over angles).
3. Reconstruct the image from the sinogram via **Filtered Back-Projection (FBP)** using several common frequency-domain filters:
   - `ramp`
   - `shepp-logan`
   - `cosine`
   - `hamming`
   - `hann`

The script displays the original phantom, the sinogram, and each FBP reconstruction, making it easy to compare the visual effects of different filters.


