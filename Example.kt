import io.ktor.application.*
import io.ktor.http.*
import io.ktor.request.receive
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*

fun main(args: Array<String>) {
    embeddedServer(Netty, 8080) {

        routing {
            this.rootSignal()
            this.rootReceive()
        }
    }.start(wait = true)
}
