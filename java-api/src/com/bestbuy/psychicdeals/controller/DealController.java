// DealController.java
package com.deals.psychicdeals.controller;

import com.deals.psychicdeals.client.AgenticAiClient;
import com.deals.psychicdeals.dto.DealRequest;
import com.deals.psychicdeals.dto.DealResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/deals")
public class DealController {

    private final AgenticAiClient agenticAiClient;

    public DealController(AgenticAiClient agenticAiClient) {
        this.agenticAiClient = agenticAiClient;
    }

    @PostMapping
    public ResponseEntity<DealResponse> getDeals(@RequestBody DealRequest request) {
        DealResponse response = agenticAiClient.fetchDeals(request);
        return ResponseEntity.ok(response);
    }
}
