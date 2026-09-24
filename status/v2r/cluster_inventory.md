# V2R cluster inventory

2026-09-24T15:24:44.005656+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026114048 available bytes; 81.92% used; 112481442 free inodes.

server1 `/home`: 324026114048 available bytes; 81.92% used; 112481442 free inodes.

server1 `/tmp`: 324026114048 available bytes; 81.92% used; 112481442 free inodes.

server1 `/var/tmp`: 324026114048 available bytes; 81.92% used; 112481442 free inodes.

server1 `/mnt/raid5`: 416774103040 available bytes; 98.09% used; 337661811 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57400872960 available bytes; 96.80% used; 110427557 free inodes.

server2 `/home`: 57400872960 available bytes; 96.80% used; 110427557 free inodes.

server2 `/tmp`: 57400872960 available bytes; 96.80% used; 110427557 free inodes.

server2 `/var/tmp`: 57400872960 available bytes; 96.80% used; 110427557 free inodes.

server2 `/mnt/raid5`: 502355283968 available bytes; 96.53% used; 445166095 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84489097216 available bytes; 95.29% used; 114159263 free inodes.

server3 `/home`: 84489097216 available bytes; 95.29% used; 114159263 free inodes.

server3 `/data`: 160416620544 available bytes; 97.78% used; 225806993 free inodes.

server3 `/tmp`: 84489097216 available bytes; 95.29% used; 114159263 free inodes.

server3 `/var/tmp`: 84489097216 available bytes; 95.29% used; 114159263 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716486144 available bytes; 94.10% used; 114348626 free inodes.

server4 `/home`: 105716486144 available bytes; 94.10% used; 114348626 free inodes.

server4 `/data`: 89426128896 available bytes; 98.76% used; 225256940 free inodes.

server4 `/tmp`: 105716486144 available bytes; 94.10% used; 114348626 free inodes.

server4 `/var/tmp`: 105716486144 available bytes; 94.10% used; 114348626 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
