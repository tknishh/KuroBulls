package main

import (

	// "bufio"
	// "fmt"
	"fmt"
	"log"
	"net"

	// "os"
	"strings"

	"github.com/gofiber/fiber"
	"github.com/gofiber/fiber/middleware"
)

// create a struct to hold spf dkim  and dmarc
type Record struct {
	HasMX    bool `json:"hasMX"`
	HasSpf   bool `json:"hasSpf"`
	HasDMARC bool `json:"hasDMARC"`
}

type Domain struct {
	DomainString string `json:"domain"`
}

func checkDomain(domain string) Record {

	var hasMX, hasSpf, hasDMARC bool
	// record := new(Record)
	var record Record

	hasMX = false
	hasDMARC = false
	hasSpf = false

	mxRecords, err := net.LookupMX(domain)
	if err != nil {
		log.Printf("Error: %v\n", err)
	}

	if len(mxRecords) > 0 {
		hasMX = true
	}

	txtRecords, err := net.LookupTXT(domain)

	if err != nil {
		log.Printf("Error: %v\n", err)
	}

	for _, record := range txtRecords {
		if strings.HasPrefix(record, "v=spf1") {
			hasSpf = true

			break
		}
	}

	dmarcRecords, err := net.LookupTXT("_dmarc." + domain)
	if err != nil {
		log.Printf("Error %v\n", err)
	}

	for _, record := range dmarcRecords {
		if strings.HasPrefix(record, "v=DMARC1") {
			hasDMARC = true
			break
		}
	}
	record.HasMX = hasMX
	record.HasDMARC = hasDMARC
	record.HasSpf = hasSpf

	return record
}

func checkEmailDomain(c *fiber.Ctx) {
	domain := new(Domain)
	if err := c.BodyParser(domain); err != nil {
		c.Status(500).Send(err)
	}

	record := checkDomain(domain.DomainString)
	c.JSON(record)

}

// func setupRoutes(app *fiber.App) {
// 	app.Post("/api/", checkEmailDomain)
// }

func main() {
	app := fiber.New()
	// setupRoutes(app)
	fmt.Println("Server started on port 3001")
	app.Post("/api/", checkEmailDomain)
	fmt.Println("Server started on port 3001")

	app.Use(middleware.Logger())
	fmt.Println("Server started on port 3001")

	app.Listen(3001)
	fmt.Println("Server started on port 3001")

}
