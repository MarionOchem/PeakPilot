package main

import (
	"PeakPilot/API/initializers"

	"github.com/gin-gonic/gin"
)

// Struct definition to represent the data of all sites_routes table data
// type all struct {
// 	Site_Name string
// 	Route_Type string
// 	Route_Count int
// }

func init() {
	initializers.LoadEnvVariables()
	initializers.ConnectToDb()
}

func main() {
	


	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "hello",
		})
	})
	r.Run() }


// GET - all routes_sites 
// func main() {
// 	// Initialize Gin
// 	router := gin.Default()

// 	// Define a route for the endpoint 
// 	router.GET("/all", getAll)

// 	// Start server
// 	router.Run("localhost:8080")
// }

// Handler function for the /all endpoint 
// func getAll(c *gin.Context) {
// 	// 1 Connect to pg db 

// 	// 2 Execute sql query : 
// 	// ECT sr.id AS site_route_id, s.name AS site_name, r.name AS route_type, sr.route_count
// 	// FROM sites_routes sr
// 	// JOIN sites s ON sr.site_name = s.id
// 	// JOIN routes r ON sr.route_type = r.id;

// 	// 3 Iterate through the query result and build a slice of all struct

// 	// 4 Return the query result as JSON
// }