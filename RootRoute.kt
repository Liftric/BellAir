import io.ktor.application.*
import io.ktor.http.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*

fun Routing.rootSignal() {
    get("/signal") {
        call.respondText("Signal", ContentType.Text.Plain)
    }
}

fun Routing.rootReceive() {
    get("/receive") {
        call.respondText("Receive", ContentType.Text.Plain)
    }

}

