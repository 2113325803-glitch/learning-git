import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.interpolate import interp1d

# 设定中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ================= 1. 基础物性数据与平衡数据 =================
# 乙醇(1) 和 水(2) 的物性常数
M1 = 46.07; M2 = 18.02
cp1 = 2.90; cp2 = 4.18
r1 = 850; r2 = 2260

# 平衡数据与泡点数据
x_data = np.array([0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.894, 1.0])
y_data = np.array([0, 0.11, 0.175, 0.273, 0.34, 0.392, 0.43, 0.495, 0.53, 0.575, 0.614, 0.657, 0.698, 0.755, 0.818, 0.894, 1.0])
ts_data = np.array([100, 97, 94, 90, 88, 86.5, 85, 83, 81.5, 80, 79, 78.5, 78.2, 78.1, 78.2, 78.2, 78.3])

f_y2x = interp1d(y_data, x_data, kind='linear', fill_value="extrapolate")
f_x2y = interp1d(x_data, y_data, kind='linear', fill_value="extrapolate")
f_x2ts = interp1d(x_data, ts_data, kind='linear', fill_value="extrapolate")

x_curve = np.linspace(0, 1, 200)
y_curve = f_x2y(x_curve)

# ================= 2. 初始化图形窗口 =================
fig, ax = plt.subplots(figsize=(9, 10))
# 【已修复】去掉了重复的 bottom 参数
plt.subplots_adjust(bottom=0.40) 

# 初始参数
init_xD = 0.744
init_xW = 0.015
init_xF = 0.056
init_R = 2.0
init_tF = 25.0

ax.plot(x_curve, y_curve, 'k-', linewidth=2, label='平衡线')
ax.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='对角线 y=x')

# 动态线对象
line_rect, = ax.plot([], [], 'r-', linewidth=2, label='精馏段操作线')
line_strip, = ax.plot([], [], 'm-', linewidth=2, label='提馏段操作线')
line_q, = ax.plot([], [], 'g-.', linewidth=1.5, label='q线 (进料线)')
line_steps, = ax.plot([], [], 'b-', linewidth=1.5, label='理论塔板 (阶梯)')

# 标记 xD 和 xW 的竖向辅助线（灰色虚线，只画到对角线）
line_v_xD, = ax.plot([], [], color='gray', linestyle=':', linewidth=2, label='塔顶/塔底边界')
line_v_xW, = ax.plot([], [], color='gray', linestyle=':', linewidth=2)

# 文本对象
text_stage = ax.text(0.3, 0.90, '', fontsize=14, color='blue', fontweight='bold')
text_q_info = ax.text(0.1, 0.80, '', fontsize=11, color='black')

# 将标签放在 x 轴下方 (y = -0.06)，并带白色背景框防止被网格线遮挡
trans = ax.get_xaxis_transform()
text_xD_val = ax.text(0, -0.06, '', transform=trans, fontsize=11, color='red', 
                      fontweight='bold', ha='center', va='top', 
                      bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))
text_xW_val = ax.text(0, -0.06, '', transform=trans, fontsize=11, color='purple', 
                      fontweight='bold', ha='center', va='top',
                      bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('液相中乙醇摩尔分数 (x)', fontsize=12)
ax.set_ylabel('气相中乙醇摩尔分数 (y)', fontsize=12)
ax.set_title('交互式乙醇-水精馏 (自带q值热力学计算)', fontsize=14, pad=15)
ax.legend(loc='lower right')
ax.grid(True, linestyle=':', alpha=0.6)

# ================= 3. 核心更新函数 =================
def update(val):
    xD = s_xD.val
    xW = s_xW.val
    xF = s_xF.val
    R = s_R.val
    tF = s_tF.val

    # 更新竖向辅助线，只画到对角线 (y = x)
    line_v_xD.set_data([xD, xD], [0, xD])
    line_v_xW.set_data([xW, xW], [0, xW])
    
    # 更新 x 轴上的文字标签位置和内容
    text_xD_val.set_text(f'xD={xD:.3f}')
    text_xW_val.set_text(f'xW={xW:.3f}')
    
    text_xD_val.set_position((xD, -0.06))
    text_xW_val.set_position((xW, -0.06))
    
    # 智能调整水平对齐方式，避免左边和右边的字跑出图外
    if xD > 0.9: text_xD_val.set_ha('right')
    elif xD < 0.1: text_xD_val.set_ha('left')
    else: text_xD_val.set_ha('center')

    if xW > 0.9: text_xW_val.set_ha('right')
    elif xW < 0.1: text_xW_val.set_ha('left')
    else: text_xW_val.set_ha('center')

    if xD <= xF or xF <= xW:
        text_stage.set_text("参数错误: 必须满足 xD > xF > xW")
        text_q_info.set_text("")
        line_rect.set_data([], [])
        line_strip.set_data([], [])
        line_q.set_data([], [])
        line_steps.set_data([], [])
        fig.canvas.draw_idle()
        return

    # --- 依据公式实时计算 q 值 ---
    ts = f_x2ts(xF)
    cpm = cp1 * M1 * xF + cp2 * M2 * (1 - xF)
    rF = r1 * M1 * xF + r2 * M2 * (1 - xF)
    q = 1 + (cpm * (ts - tF)) / rF
    
    text_q_info.set_text(f"当前 tF={tF:.1f}℃, 泡点 ts={ts:.1f}℃\n计算得 q = {q:.3f}")

    # --- 计算操作线 ---
    slope_rect = R / (R + 1)
    intercept_rect = xD / (R + 1)
    x_rect_plot = np.linspace(xF, xD, 10)
    line_rect.set_data(x_rect_plot, slope_rect * x_rect_plot + intercept_rect)

    if abs(q - 1.0) < 0.001: 
        x_q = xF
        y_q = slope_rect * x_q + intercept_rect
        x_q_plot = [xF, xF]
        y_q_plot = [xF, y_q]
    else: 
        slope_q = q / (q - 1)
        intercept_q = -xF / (q - 1)
        x_q = (intercept_rect - intercept_q) / (slope_q - slope_rect)
        y_q = slope_rect * x_q + intercept_rect
        x_q_plot = np.linspace(xF, x_q, 10)
        y_q_plot = slope_q * x_q_plot + intercept_q
    
    line_q.set_data(x_q_plot, y_q_plot)

    if abs(x_q - xW) < 1e-5:
        slope_strip = 0
    else:
        slope_strip = (y_q - xW) / (x_q - xW)
    intercept_strip = xW - slope_strip * xW
    x_strip_plot = np.linspace(xW, x_q, 10)
    line_strip.set_data(x_strip_plot, slope_strip * x_strip_plot + intercept_strip)

    # --- 画阶梯 ---
    x_curr = xD
    y_curr = xD
    stage = 0
    x_steps = [x_curr]
    y_steps = [y_curr]

    while x_curr > xW:
        stage += 1
        x_eq = f_y2x(y_curr)
        x_steps.append(x_eq)
        y_steps.append(y_curr)
        
        if x_eq > x_q: 
            y_next = slope_rect * x_eq + intercept_rect
        else:
            y_next = slope_strip * x_eq + intercept_strip
            
        x_steps.append(x_eq)
        y_steps.append(y_next)
        
        x_curr = x_eq
        y_curr = y_next

        if stage > 200:
            text_stage.set_text("警告: 塔板数 > 200")
            break
    else:
        text_stage.set_text(f'理论塔板数 = {stage}')

    line_steps.set_data(x_steps, y_steps)
    fig.canvas.draw_idle()

# ================= 4. 添加滑块 =================
ax_xD = plt.axes([0.15, 0.28, 0.65, 0.03])
ax_xW = plt.axes([0.15, 0.23, 0.65, 0.03])
ax_xF = plt.axes([0.15, 0.18, 0.65, 0.03])
ax_R  = plt.axes([0.15, 0.13, 0.65, 0.03])
ax_tF = plt.axes([0.15, 0.08, 0.65, 0.03])

s_xD = Slider(ax_xD, '塔顶 xD', 0.2, 0.95, valinit=init_xD, valstep=0.005)
s_xW = Slider(ax_xW, '塔底 xW', 0.001, 0.1, valinit=init_xW, valstep=0.001)
s_xF = Slider(ax_xF, '进料 xF', 0.02, 0.5, valinit=init_xF, valstep=0.005)
s_R  = Slider(ax_R, '回流比 R', 0.5, 10.0, valinit=init_R, valstep=0.1)
s_tF = Slider(ax_tF, '进料温度 tF', 10.0, 100.0, valinit=init_tF, valstep=1.0)

s_xD.on_changed(update)
s_xW.on_changed(update)
s_xF.on_changed(update)
s_R.on_changed(update)
s_tF.on_changed(update)

update(None)
plt.show()