import pathlib


def main():
    with open(pathlib.Path(__file__).parent / 'notes.txt') as inf:
        n_priests = int(inf.read().strip())

    blocks_needed = 1
    layer_widths = []
    thickness = 0
    n_acolytes = 5
    n_blocks = 50



    while n_blocks > blocks_needed:
        n_blocks -= blocks_needed
        
        if not layer_widths:
            layer_widths += [1]
            thickness = 1
        
        thickness = (thickness * n_priests) % n_acolytes

        blocks_needed = 0
        new_layer_widths = []

        for i in range(thickness):
            try:
                old_thickness = layer_widths[i]
            except IndexError:
                old_thickness = 0

            blocks_needed += thickness - old_thickness
            new_layer_widths.append(thickness)

        new_layer_widths.extend(layer_widths)

        for i, w in enumerate(new_layer_widths[thickness:], start=thickness):
            try:
                old_thickness = layer_widths[i]
            except IndexError:
                old_thickness = 0
            blocks_needed += w - old_thickness

        width = layer_widths[0]
        layer_widths = new_layer_widths


        

    result = (width + 2) * (blocks_needed - n_blocks)

    print(result)

if __name__ == "__main__":
    main()