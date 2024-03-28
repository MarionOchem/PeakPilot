package main

import (
	"PeakPilot/API/controllers"
	"PeakPilot/API/initializers"

	"github.com/gin-gonic/gin"
)


func init() {
	initializers.LoadEnvVariables()
	initializers.ConnectToDb()
}

func main() {
	r := gin.Default()
	r.GET("/", controllers.GetAll)
	r.GET("/sites", controllers.GetSite)
	r.GET("/routes", controllers.GetRoutes)
	r.GET("/:site", controllers.GetSpecificSite) // Get only a specific site routes data
	r.GET("/:site/:route", controllers.GetSpecificSiteRoute) // Get only a specific site and specific route data
	r.Run() }
