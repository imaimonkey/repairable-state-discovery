# V2R cluster inventory

2026-09-24T03:28:54.637682+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325353746432 available bytes; 81.85% used; 112498178 free inodes.

server1 `/home`: 325353746432 available bytes; 81.85% used; 112498178 free inodes.

server1 `/tmp`: 325353746432 available bytes; 81.85% used; 112498178 free inodes.

server1 `/var/tmp`: 325353746432 available bytes; 81.85% used; 112498178 free inodes.

server1 `/mnt/raid5`: 405608857600 available bytes; 98.14% used; 337733684 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40841003008 available bytes; 97.72% used; 110431110 free inodes.

server2 `/home`: 40841003008 available bytes; 97.72% used; 110431110 free inodes.

server2 `/tmp`: 40841003008 available bytes; 97.72% used; 110431110 free inodes.

server2 `/var/tmp`: 40841003008 available bytes; 97.72% used; 110431110 free inodes.

server2 `/mnt/raid5`: 527274405888 available bytes; 96.36% used; 445198000 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292372852736 available bytes; 83.68% used; 114201025 free inodes.

server3 `/home`: 292372852736 available bytes; 83.68% used; 114201025 free inodes.

server3 `/data`: 36017344512 available bytes; 99.50% used; 225843047 free inodes.

server3 `/tmp`: 292372852736 available bytes; 83.68% used; 114201025 free inodes.

server3 `/var/tmp`: 292372852736 available bytes; 83.68% used; 114201025 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987121152 available bytes; 94.09% used; 114349606 free inodes.

server4 `/home`: 105987121152 available bytes; 94.09% used; 114349606 free inodes.

server4 `/data`: 283505860608 available bytes; 96.08% used; 225385620 free inodes.

server4 `/tmp`: 105987121152 available bytes; 94.09% used; 114349606 free inodes.

server4 `/var/tmp`: 105987121152 available bytes; 94.09% used; 114349606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
