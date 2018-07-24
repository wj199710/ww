/**
  * Created by Administrator on 2018/7/24.
  */
object weather {
  def main(args: Array[String]) {
    var temp=List(30,32,28,25,20,30,27)
    println("天气列表如下："+temp)
    for(i<-Range(0,7) if i==2){
      println("星期三的温度"+temp(i))
    }
  }

}

