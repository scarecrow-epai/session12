import calculator.sin, calculator.cos, calculator.tan, calculator.sigmoid, calculator.relu, calculator.tanh, calculator.softmax, calculator.log, calculator.exp
from calculator.sin import calc_d_sin

print(f"sin(10) = {calculator.sin.calc_sin(10)}")
print(f"cos(10) = {calculator.cos.calc_cos(10)}")
print(f"tan(10) = {calculator.tan.calc_tan(10)}")
print(f"sigmoid(0.7) = {calculator.sigmoid.calc_sigmoid(0.7)}")
print(f"relu(0.7) = {calculator.relu.calc_relu(0.7)}")
print(f"tanh(0.7) = {calculator.tanh.calc_tanh(0.7)}")
print(f"softmax(1, 2, 3) = {calculator.softmax.calc_softmax([1, 2, 3])}")
print(f"log(10) = {calculator.log.calc_log(10)}")
print(f"exp(10) = {calculator.exp.calc_exp(10)}")

print("\n ************* \n")

print(
    f"derivative sin(-0.5440211108893698) = {calculator.sin.calc_d_sin(-0.5440211108893698)}"
)
print(
    f"derivative cos(-0.8390715290764524) = {calculator.cos.calc_d_cos(-0.8390715290764524)}"
)
print(
    f"derivative tan(0.6483608274590866) = {calculator.tan.calc_d_tan(0.6483608274590866)}"
)
print(
    f"derivative sigmoid(0.6681877721681662) = {calculator.sigmoid.calc_d_sigmoid(0.6681877721681662)}"
)
print(f"derivative relu(0.7) = {calculator.relu.calc_d_relu(0.7)}")
print(
    f"derivative tanh(0.6043677771171636) = {calculator.tanh.calc_d_tanh(0.6043677771171636)}"
)
print(
    f"derivative softmax(0.09003057317038046, 0.24472847105479767, 0.6652409557748219) = {calculator.softmax.calc_d_softmax([0.09003057317038046, 0.24472847105479767, 0.6652409557748219])}"
)
print(
    f"derivative log(2.302585092994046) = {calculator.log.calc_d_log(2.302585092994046)}"
)
print(f"derivative exp(10) = {calculator.exp.calc_d_exp(10)}")
