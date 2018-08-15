'''
简述 进程、线程、协程的区别 以及应用场景？
进程拥有自己独立的堆和栈，既不共享堆，亦不共享栈，进程由操作系统调度。
线程拥有自己独立的栈和共享的堆，共享堆，不共享栈，线程亦由操作系统调度(标准线程是的)。
协程和线程一样共享堆，不共享栈，协程由程序员在协程的代码里显示调度。
进程和其他两个的区别还是很明显的
协程和线程的区别是：协程避免了无意义的调度，由此可以提高性能，
但也因此，程序员必须自己承担调度的责任，同时，协程也失去了标准线程使用多CPU的能力。

堆与栈的区别很明显：
    1.栈内存存储的是局部变量而堆内存存储的是实体；
    2.栈内存的更新速度要快于堆内存，因为局部变量的生命周期很短；
    3.栈内存存放的变量生命周期一旦结束就会被释放，而堆内存存放的实体会被垃圾回收机制不定时的回收

进程：充分利用多CPU
线程：充分利用多核（达到真正的多任务并行）
协程：充分利用单核（充分挖掘不断提高性能的单核CPU的潜力。类比事件驱动和异步程序）。
      既可以利用异步优势，又可以避免反复系统调用，还有进程切换造成的开销。
协程存在的意义： 
  对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继续）。
  协程，则只使用一个线程，在一个线程中规定某个代码块执行顺序。
  协程能保留上一次调用时的状态，不需要像线程一样用回调函数，所以性能上会有提升。
缺点：本质是个单线程，不能利用到单个CPU的多个核。
线程和进程的操作是由程序触发系统接口，最后的执行者是系统；协程的操作则是程序员。
切换开销（即调度和切换的时间）：进程 > 线程 > 协程

更加具象的解释：
  一开始大家想要同一时间执行那么三五个程序，大家能一块跑一跑。特别是UI什么的，别一上计算量比较大的玩意就跟死机一样。
于是就有了并发，从程序员的角度可以看成是多个独立的逻辑流。
内部可以是多cpu并行，也可以是单cpu时间分片，能快速的切换逻辑流，看起来像是大家一块跑的就行。

  但是一块跑就有问题了。我计算到一半，刚把多次方程解到最后一步，你突然插进来，我的中间状态咋办，我用来储存的内存被你覆盖了咋办？
所以跑在一个cpu里面的并发都需要处理上下文切换的问题。
进程就是这样抽象出来个一个概念，搭配虚拟内存、进程表之类的东西，用来管理独立的程序运行、切换。

  后来一电脑上有了好几个cpu，好咧，大家都别闲着，一人跑一进程。就是所谓的并行。

  因为程序的使用涉及大量的计算机资源配置，把这活随意的交给用户程序，非常容易让整个系统分分钟被搞跪，资源分配也很难做到相对的公平。
所以核心的操作需要陷入内核(kernel)，切换到操作系统，让老大帮你来做。

  因为程序的使用涉及大量的计算机资源配置，把这活随意的交给用户程序，非常容易让整个系统分分钟被搞跪，资源分配也很难做到相对的公平。
所以核心的操作需要陷入内核(kernel)，切换到操作系统，让老大帮你来做。

  如果连时钟阻塞、 线程切换这些功能我们都不需要了，自己在进程里面写一个逻辑流调度的东西。
那么我们即可以利用到并发优势，又可以避免反复系统调用，还有进程切换造成的开销，分分钟给你上几千个逻辑流不费力。
这就是用户态线程。

  从上面可以看到，实现一个用户态线程有两个必须要处理的问题：一是碰着阻塞式I\O会导致整个进程被挂起；
二是由于缺乏时钟阻塞，进程需要自己拥有调度线程的能力。如果一种实现使得每个线程需要自己通过调用某个方法，主动交出控制权。
那么我们就称这种用户态线程是协作式的，即是协程。

本质上协程就是用户空间下的线程。
