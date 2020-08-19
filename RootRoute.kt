import io.ktor.application.*
import io.ktor.features.*
import io.ktor.http.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*

fun Routing.rootSignal() {
    install(StatusPages) {
        exception<Throwable> { e ->
            call.respondText(e.localizedMessage, ContentType.Text.Plain, HttpStatusCode.InternalServerError)
        }
    }
    install(ContentNegotiation) {
        //moshi()
    }

    post("/signal") {
        val parameters = call.receiveParameters()

        val paramValue1 = parameters["id"]
        val paramValue2 = parameters["timestamp"]

        call.respondText("Received signal $paramValue1 and $paramValue2\n")
    }
}

fun Routing.rootReceive() {
    get("/receive") {
        call.respondText("This is a GET route")
    }

}

