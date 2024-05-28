public class MathUtils {

public int complexCalculation(int a, int b, int c, int d) {

int result = 0;

if (a > b) {

result = a + b;

if (c > d) {

result *= c;

if (result > 1000) {

result -= 100;

} else {

result += 100;

}

} else {

result *= d;

if (result < 500) {

result /= 2;

} else {

result *= 2;

}

}

} else {

result = b - a;

if (c < d) {

result += c;

if (result % 2 == 0) {

result /= 2;

} else {

result *= 3;

}

} else {

result -= d;

if (result < 0) {

result = -result;

} else {

result += 50;

}

}

}

return result;

}

}