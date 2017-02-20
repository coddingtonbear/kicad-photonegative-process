import os
import sys

import pcbnew

LAYERS = {
    # Items should match the following format; all fields are optional::
    #
    #     pcbnew.F_Cu: {
    #         'name': 'F.Cu',
    #         'description': 'Front Copper (Top Layer)',
    #         'mirrored': True,
    #         'negative': True,
    #     }
    #
    pcbnew.F_Cu: {
        'description': 'Front Copper (Top Layer)',
        'mirrored': True,
        'negative': True,
    },
    pcbnew.B_Cu: {
        'description': 'Back Copper (Bottom Layer)',
        'negative': True,
    },
    pcbnew.F_Mask: {
        'description': 'Front Mask',
        'mirrored': True,
    },
    pcbnew.B_Mask: {
        'description': 'Back Mask',
    },
    pcbnew.F_Paste: {
        'description': 'Front Solder Paste',
        'mirrored': True,
    },
    pcbnew.B_Paste: {
        'description': 'Back Solder Paste',
    }
}


def plot(board_filename=None, layers=None):
    if board_filename is None:
        board = pcbnew.GetBoard()
    else:
        board = pcbnew.LoadBoard(os.path.expanduser(board_filename))

    if layers is None:
        layers = LAYERS
    elif isinstance(layers, list):
        layers = layers.keys()

    plot_ctrl = pcbnew.PLOT_CONTROLLER(board)

    plot_opts = plot_ctrl.GetPlotOptions()
    plot_opts.SetPlotFrameRef(False)
    plot_opts.SetLineWidth(pcbnew.FromMM(0.35))
    plot_opts.SetAutoScale(False)
    plot_opts.SetScale(1)
    plot_opts.SetUseGerberAttributes(True)
    plot_opts.SetExcludeEdgeLayer(False)
    plot_opts.SetUseAuxOrigin(False)
    plot_opts.SetPlotViaOnMaskLayer(True)

    for layer, layer_info in layers.items():
        layer_name = layers.get('name', board.GetLayerName(layer))
        plot_opts.SetMirror(layer_info.get('mirrored', False))
        plot_opts.SetNegative(layer_info.get('negative', False))
        plot_ctrl.SetLayer(layer)
        plot_ctrl.OpenPlotfile(
            layer_name,
            pcbnew.PLOT_FORMAT_PDF,
            layer_info.get('description', layer_name)
        )
        plot_ctrl.PlotLayer()


if __name__ == '__main__':
    plot(sys.argv[1])
