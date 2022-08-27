import java.util.function.Function;
import javax.lang.model.type.NullType;

public interface Monad <T, E> {

    public Monad<T, NullType> return_();
    public Monad<NullType, E> bind(Function<T, Monad<NullType, E>> f);
    public Monad<NullType, E> sequencer(Monad<NullType, E> b);

    public T extractLeft();
    public E extractRight();


    public class Kek<T, E> implements Monad<T,E> {

        private T left;
        private E right;

        public Kek(T left, E right) {
            this.left = left;
            this.right = right;
        }

        public T extractLeft() {
            return this.left;
        }

        public E extractRight() {
            return this.right;
        }


        public Monad<T, NullType> return_() {
            return new Kek<T, NullType>((T) this.left, null);
        }

        public Monad<NullType, E> bind(Function<T, Monad<NullType, E>> f) {
            return f.apply((T) left);
        }

        public Monad<NullType, E> sequencer(Monad<NullType, E> b) {
            return bind(__ -> b);
        }


    }


    public static void main(String[] args) {
        Kek<Object,Object> three = new Kek<>(3, null);

        System.out.println(three.return_().extractLeft());
        System.out.println(three.bind(k -> new Kek((int) k + 2, null)).extractLeft());
        System.out.println(three.sequencer(new Kek(null, "kek")).extractRight());
    }
}
