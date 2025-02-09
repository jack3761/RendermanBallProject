# RenderMan Massage Ball Shader and Rendering Project

## Overview
This project explores the use of Pixar's RenderMan and Open Shading Language (OSL) to create a physically accurate render of a massage ball. The goal was to replicate the object's real-world appearance by focusing on procedural modeling, shading, and rendering techniques.

## Features
- **Procedural Modeling**: Generates the spikes using a displacement-based approach.
- **Custom Shader Development**: Implements an OSL shader for defining surface properties such as roughness, specularity, and surface wear.
- **Physically-Based Rendering**: Utilizes RenderMan’s PxrDisney BRDF for a convincing material representation.
- **Procedural Surface Details**: Adds wear effects such as spike tip erosion, blotches, and minor imperfections to enhance realism.
- **Realistic Scene Composition**: Incorporates HDRI lighting and depth of field for photorealistic rendering.

## Implementation
### 1. **Modeling**
- **Displacement-Based Spike Generation**: Instead of manually placing spikes, a procedural displacement approach was used to achieve efficiency and flexibility.
- **Surface Refinements**: Additional displacement was applied to create the seam around the ball’s equator, improving authenticity.

### 2. **Shading & Materials**
- **BRDF Choice**: The PxrDisney BRDF was selected for its ability to handle the varying roughness and specularity between the ball’s smooth surface and its rough spikes.
- **Procedural Adjustments**: Roughness and specularity dynamically change across the surface to mimic real-world materials.
- **Surface Wear Effects**: Procedural noise functions simulate wear, adding realism through controlled variations.

### 3. **Procedural Enhancements**
- **Spike Roughness Variation**: A periodic mod function was used to introduce fine-scale texture variations.
- **Wear at Spike Tips**: Different shading responses were applied to the tips, simulating natural erosion from usage.
- **Main Surface Detail**: Subtle procedural noise was added to mimic manufacturing imperfections and dirt accumulation.

### 4. **Rendering Setup**
- **HDRI-Based Lighting**: Environment maps provide realistic reflections and natural light distribution.
- **Depth of Field**: A shallow depth of field (f/1.4) was used to emphasize the massage ball.
- **Scene Integration**: A wooden table surface was used as a base, textured using RenderMan’s material library.

## Results
Two key renders were produced:
1. A close-up showcasing the spike roughness and surface imperfections.
2. A full-object render with an overhead perspective and alternate lighting conditions.

## Dependencies
- Pixar RenderMan
- Open Shading Language (OSL)
- Python (for initial procedural modeling tests)

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/massage-ball-renderman.git
   ```
2. Open the RenderMan scene file.
3. Ensure the OSL shader files are compiled and assigned in the material setup.
4. Render using the provided scene settings or modify parameters as needed.

## Future Improvements
- Extend procedural texturing for finer surface details.
- Experiment with alternative lighting setups for enhanced material representation.
- Expand procedural modeling techniques to other complex objects.

## Author
**Jack Purkiss**  
NCCA, Bournemouth University  
Email: s5603002@bournemouth.ac.uk

