import java.util.Arrays;
import java.util.function.Function;


public class Mapper<T> {

    public T[] map(Function<T,T> func, T[] arr) {

        T[] mapped = (T[]) new Object[arr.length];

        for (int i = 0; i < arr.length; i++) {
            mapped[i] = func.apply(arr[i]);
        }

        return mapped;
    }


    public static void main(String[] args) {
        Function<Integer, Integer> poopoo = k -> k + 1;
        Mapper<Integer> intmap = new Mapper<>();
        Integer[] kek = {3, 1, -1};

        Object[] bigkek = intmap.map(poopoo, kek);
        System.out.println(Arrays.toString(bigkek));
    }
}


// output:
// [4, 2, 0]
