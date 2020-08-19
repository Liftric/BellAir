plugins {
    kotlin("jvm") version "1.3.72"
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
    jcenter()
}

dependencies {
    implementation("io.ktor:ktor-server-netty:1.3.2")
    implementation(kotlin("stdlib"))
    testCompile("junit", "junit", "4.12")
    implementation(kotlin("script-runtime"))
}
