// DealController.java
package com.bestbuy.psychicdeals.controller;

import com.bestbuy.psychicdeals.client.AgenticAiClient;
import com.bestbuy.psychicdeals.dto.DealRequest;
import com.bestbuy.psychicdeals.dto.DealResponse;
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
