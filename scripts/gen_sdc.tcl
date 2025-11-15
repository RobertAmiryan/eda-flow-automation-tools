#!/usr/bin/env tclsh
# Simple SDC generator that reads a YAML config and outputs SDC constraints to stdout.
# Usage: tclsh gen_sdc.tcl configs/example_sdc_config.yaml > out.sdc
package require yaml 1.0  ;# Not guaranteed in all environments; using simple parsing below

if {[llength $argv] < 1} {
    puts stderr "Usage: gen_sdc.tcl <sdc_config.yaml>"
    exit 1
}
set fname [lindex $argv 0]
# Read file contents
set fh [open $fname r]
set content [read $fh]
close $fh

# Very small YAML-ish parser for the simple structures we produce (does NOT handle all YAML)
# This is intentionally lightweight to avoid external dependencies.
set lines [split $content "\n"]
set clocks {}
set in_clocks 0
set in_input_delays 0
set in_output_delays 0
foreach l $lines {
    set line [string trim $l]
    if {$line == "clocks:"} { set in_clocks 1; set in_input_delays 0; set in_output_delays 0; continue }
    if {$line == "input_delays:"} { set in_clocks 0; set in_input_delays 1; set in_output_delays 0; continue }
    if {$line == "output_delays:"} { set in_clocks 0; set in_input_delays 0; set in_output_delays 1; continue }
    if {$in_clocks && [regexp {^- name: (.+)$} $line -> name]} {
        # next lines expected period and ports
        set name [string trim [string range $name 0 end]]
        # find following lines
        # naive scan
        set period 1.0
        set ports {}
        # look ahead (simple)
        # This is intentionally permissive; for robust usage prefer a Python/YAML pipeline.
        continue
    }
    if {$in_clocks && [regexp {period_ns: ([0-9\.]+)} $line -> p]} {
        set period $p
        puts "create_clock -name clk -period $period"
    }
    if {$in_input_delays && [regexp {^- port: (.+)$} $line -> p]} {
        set port $p
    }
    if {$in_input_delays && [regexp {delay_ns: ([0-9\.]+)} $line -> d]} {
        puts "set_input_delay $d -clock clk_core [get_ports ${port}] ;# example" 
    }
}
# Basic example header
puts "# Generated SDC (simple example)"
puts "# Add clocks and IO constraints as required"
