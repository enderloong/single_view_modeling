import predpos as pps
import vp_rw as vpr

# control variables
class proc_control():
    mode = 'i'
    input_mode = 'a'
    debug = True
    mouse_pos = [0, 0]
    max_clk = 4
    clk_pt = [[0, 0]] * max_clk
    cc_num = 0

    def reset(self):
        self.mode = 'i'
        self.clk_pt =[[0,0]] * self.max_clk
        self.cc_num = 0

    def mode_inp(self):
        if self.cc_num < 3:
            self.clk_pt[self.cc_num] = self.mouse_pos
            self.cc_num += 1
        else:
            pred_pos = pps.pred_p(self.clk_pt[0], self.clk_pt[1], self.clk_pt[2], self.mouse_pos)
            if self.debug:
                print([self.clk_pt[0], self.clk_pt[1], self.clk_pt[2], self.mouse_pos])
                print('predicted position:', pred_pos)
            self.clk_pt[self.cc_num] = pred_pos
            self.cc_num += 1
            self.mode = 'fp'
    
    def mode_vp(self, img):
        print(self.clk_pt)
        vp = vpr.compute_vp(self)
        img.info_2d.vp = vp
        if self.debug:
            print('[DEBUG]vanished point of this plane: ', img.info_2d.vp)
        self.mode = 'f_vp'

    def mousedown(self):
        if self.debug:
            print('click on:', [self.mouse_pos[0], self.mouse_pos[1]])
            #print('current mode:', self.mode)
        if self.mode == 'in_plane':
            self.mode_inp()
            

        