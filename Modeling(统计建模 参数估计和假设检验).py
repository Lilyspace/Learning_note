统计学建模：参数估计和假设检验

中心极限定理：点估计    样本的统计就是总体均值的无偏估计
              区间估计  在给定的置信区间水平alha下，确定出置信区间，该区间会以alpha的概率包含总体的均值
点估计
point_estimates=[]
for x in range(500): #500 次循环
    sample=np.random.choice(a=my_data,size=100) # 每次随机抽样 100 个样本
    point_estimates.append(sample.mean())
pd.DataFrame(point_estimates).hist(bins=40) # 均值大致呈钟型分布
print('样本均值的均值为: ', np.array(point_estimates).mean())

区间估计
sample_size=100
sample=np.random.choice(a=my_data,size=sample_size)
sigma=sample.std()/(sample_size)**0.5
stats.t.interval(alpha=0.95, # 置信水平 confidence level
df=sample_size-1, # 自由度 Degrees of freedom
loc=sample.mean(),
scale=sigma)
# 返回拥有 95% 置信水平的置信区间


假设检验
1.提出空假设和替代假设
2.选择显著性水平，进行合适的检验
3.将p值与显著性水平比较
4.接受或拒绝空假设

P值：基于当前样本和空假设，现有统计量落入当前值及以外区域的概率（可理解为，接受空假设有P的可能性不对）
显著性水平alpha:拒绝接受空假设的门限；p值>alpha 为接受域，p值<alpha 为拒绝域
本质：P值与alpha都是反应I型错误率（I型错误：空假设为真，拒绝假设；II型错误:替代假设为真，拒绝替代假设）
