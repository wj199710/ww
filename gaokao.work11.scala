import scala.collection.mutable.ListBuffer

/**
  * Created by Administrator on 2018/7/24.
  */
object gaokao {
  def main(args: Array[String]) {
      import org.json.JSONObject//导入str转json工具包
      import org.apache.spark.SparkConf//
      import org.apache.spark.SparkContext
      //sparkcontext的配置，运行在本地，名称为cala
      val conf = new SparkConf().setAppName("cala").setMaster("local").set("spark.testing.memory","2147480000")
      val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
      //使用spark读取文本文件
      sc.textFile("C:\\Users\\Administrator\\第三组黑吉上数据.txt")
        .filter(line=>line.endsWith("status\":1}"))
        .flatMap(line=>{//line str===>List line  抚平
        val  json = new JSONObject(line)
          val jsonlist = json.getJSONArray("data")
          //        jsonlist.getJSONObject(0)
          val list = ListBuffer[JSONObject]()
          for(i<-0 to jsonlist.length()-1){
            list.append(jsonlist.getJSONObject(i))
          }
          list
        })
        .map(line=>(line.getString("school"),line.getString("plan").toInt))
        .reduceByKey(_+_)
        .foreach(line=>println(line))
    }
}
