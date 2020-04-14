
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

def createChain(block_fn,args_dict,start_from,base_name,multiple,widths,colors):
    name = base_name + "1"
    args_dict['name'] = name
    args_dict['to'] = start_from
    args_dict['width'] = widths[0]
    args_dict['color'] = colors[0]
    arr = [block_fn(**args_dict)]
    arr.append(block_fn(**args_dict))
    for i in range(1,multiple):
        new_name = base_name + str(1+i)
        args_dict['name'] = new_name
        args_dict['to'] = "("+name +"-east)"
        args_dict['width'] = widths[i]
        args_dict['color'] = colors[i]   
        arr.append(block_fn(**args_dict))
        name = new_name
    return arr
    
arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    #input
    to_input( '../examples/fcn8s/cats.jpg' ),
    *createChain(to_Conv,\
        {'s_filer':256, 'n_filer':64, 'offset':"(2,0,0)", 'height':100, 'depth':100, 'width':2,'color':'red,15'},\
        start_from="(0,0,0)",\
        base_name='ccr_b1',\
        multiple=4,
        widths = [4,2,10,2],
        colors = ['white,15','orange,10','orange,15','orange,15']),
    *createChain(to_Conv,\
        {'s_filer':256, 'n_filer':64, 'offset':"(2,0,0)", 'height':60, 'depth':60, 'width':2,'color':'red,15'},\
        start_from="(ccr_b14-east)",\
        base_name='ccr_b2',\
        multiple=4,
        widths = [10,2,20,2],
        colors = ['white,15','orange,15','orange,15','orange,15']),
     *createChain(to_Conv,\
        {'s_filer':256, 'n_filer':64, 'offset':"(1,0,0)", 'height':40, 'depth':40, 'width':2,'color':'red,15,15'},\
        start_from="(ccr_b24-east)",\
        base_name='ccr_b3',\
        multiple=4,
        widths = [20,2,35,2],
        colors = ['white,15','orange,15','orange,15','orange,15']),
     *createChain(to_Conv,\
        {'s_filer':256, 'n_filer':64, 'offset':"(1,0,0)", 'height':20, 'depth':20, 'width':2,'color':'red,15'},\
        start_from="(ccr_b34-east)",\
        base_name='ccr_b4',\
        multiple=4,
        widths = [25,2,40,2],
        colors = ['white,15','orange,15','orange,15','orange,15']),

    #block-001,
    # to_Conv('ccr_b2', 512, 64, offset="(3,0,0)", to="(ccr_b1-east)", height=64, depth=64, width=4,color='red,15,15' ),
    # to_connection( "ccr_b1", "ccr_b2"),
    # to_Conv('ccr_b3', 512, 64, offset="(3,0,0)", to="(ccr_b2-east)", height=64, depth=64, width=2,color='red,15,15' ),
    # to_connection( "ccr_b2", "ccr_b3"),
    # to_Conv('ccr_b4', 512, 64, offset="(3,0,0)", to="(ccr_b3-east)", height=64, depth=64, width=10,color='red,15' ),
    # to_connection( "ccr_b3", "ccr_b4"),
    # to_Conv('ccr_b5', 512, 64, offset="(3,0,0)", to="(ccr_b4-east)", height=64, depth=64, width=2,color='red,15' ),
    # to_connection( "ccr_b4", "ccr_b5"),
    # to_Conv('ccr_b6', 512, 64, offset="(3,0,0)", to="(ccr_b5-east)", height=40, depth=40, width=14,color='white,15' ),
    # to_connection( "ccr_b5", "ccr_b6"),
    # to_Conv('ccr_b7', 512, 64, offset="(3,0,0)", to="(ccr_b6-east)", height=40, depth=40, width=2,color='red,15' ),
    # to_connection( "ccr_b6", "ccr_b7"),
    # to_Conv('ccr_b8', 512, 64, offset="(3,0,0)", to="(ccr_b7-east)", height=40, depth=40, width=14,color='red,15' ),
    # to_connection( "ccr_b7", "ccr_b8"),
    # to_Conv('ccr_b9', 512, 64, offset="(3,0,0)", to="(ccr_b8-east)", height=40, depth=40, width=2,color='red,15' ),
    # to_connection( "ccr_b8", "ccr_b9"),
    # to_Pool(name="pool_b1", offset="(0,0,0)", to="(ccr_b1-east)", width=1, height=32, depth=32, opacity=0.5),
    
    # *block_2ConvPool( name='b2', botton='pool_b1', top='pool_b2', s_filer=256, n_filer=128, offset="(1,0,0)", size=(32,32,3.5), opacity=0.5 ),
    # *block_2ConvPool( name='b3', botton='pool_b2', top='pool_b3', s_filer=128, n_filer=256, offset="(1,0,0)", size=(25,25,4.5), opacity=0.5 ),
    # *block_2ConvPool( name='b4', botton='pool_b3', top='pool_b4', s_filer=64,  n_filer=512, offset="(1,0,0)", size=(16,16,5.5), opacity=0.5 ),

    # #Bottleneck
    # #block-005
    # to_ConvConvRelu( name='ccr_b5', s_filer=32, n_filer=(1024,1024), offset="(2,0,0)", to="(pool_b4-east)", width=(8,8), height=8, depth=8, caption="Bottleneck"  ),
    # to_connection( "pool_b4", "ccr_b5"),

    # #Decoder
    # *block_Unconv( name="b6", botton="ccr_b5", top='end_b6', s_filer=64,  n_filer=512, offset="(2.1,0,0)", size=(16,16,5.0), opacity=0.5 ),
    # to_skip( of='ccr_b4', to='ccr_res_b6', pos=1.25),
    # *block_Unconv( name="b7", botton="end_b6", top='end_b7', s_filer=128, n_filer=256, offset="(2.1,0,0)", size=(25,25,4.5), opacity=0.5 ),
    # to_skip( of='ccr_b3', to='ccr_res_b7', pos=1.25),    
    # *block_Unconv( name="b8", botton="end_b7", top='end_b8', s_filer=256, n_filer=128, offset="(2.1,0,0)", size=(32,32,3.5), opacity=0.5 ),
    # to_skip( of='ccr_b2', to='ccr_res_b8', pos=1.25),    
    
    # *block_Unconv( name="b9", botton="end_b8", top='end_b9', s_filer=512, n_filer=64,  offset="(2.1,0,0)", size=(40,40,2.5), opacity=0.5 ),
    # to_skip( of='ccr_b1', to='ccr_res_b9', pos=1.25),
    
    # to_ConvSoftMax( name="soft1", s_filer=512, offset="(0.75,0,0)", to="(end_b9-east)", width=1, height=40, depth=40, caption="SOFT" ),
    # to_connection( "end_b9", "soft1"),
     
    to_end() 
    ]
print(arch)

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
