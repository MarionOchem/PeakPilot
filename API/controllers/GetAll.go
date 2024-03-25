package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)

// Struct definition to represent the data of all sites_routes table data
type SitesRoutes struct {
	SiteName string
	RouteType string
	RouteCount int 
}

func GetAll(c *gin.Context) {
	// Get all
	var sitesRoutes []SitesRoutes
	result := initializers.DB.Table("sites_routes").
	Select("sites_routes.id AS site_route_id, sites.name AS site_name, routes.name AS route_type, sites_routes.route_count").
	Joins("JOIN sites ON sites_routes.site_name = sites.id").
	Joins("JOIN routes ON sites_routes.route_type = routes.id").
	Find(&sitesRoutes)
	
	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Return the list of sites in the JSON response
	c.JSON(http.StatusOK, gin.H{
		"message": "All routes of all sites",
		"sites":   sitesRoutes,
	})
}

