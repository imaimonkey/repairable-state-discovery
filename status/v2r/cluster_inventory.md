# V2R cluster inventory

2026-09-26T02:36:24.679148+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318419050496 available bytes; 82.24% used; 112476271 free inodes.

server1 `/home`: 318419050496 available bytes; 82.24% used; 112476271 free inodes.

server1 `/tmp`: 318419050496 available bytes; 82.24% used; 112476271 free inodes.

server1 `/var/tmp`: 318419050496 available bytes; 82.24% used; 112476271 free inodes.

server1 `/mnt/raid5`: 331164483584 available bytes; 98.48% used; 337546100 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942887936 available bytes; 98.72% used; 110406222 free inodes.

server2 `/home`: 22942887936 available bytes; 98.72% used; 110406222 free inodes.

server2 `/tmp`: 22942887936 available bytes; 98.72% used; 110406222 free inodes.

server2 `/var/tmp`: 22942887936 available bytes; 98.72% used; 110406222 free inodes.

server2 `/mnt/raid5`: 288786128896 available bytes; 98.00% used; 445054095 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84316991488 available bytes; 95.29% used; 114152376 free inodes.

server3 `/home`: 84316991488 available bytes; 95.29% used; 114152376 free inodes.

server3 `/data`: 124787564544 available bytes; 98.28% used; 225816879 free inodes.

server3 `/tmp`: 84316991488 available bytes; 95.29% used; 114152376 free inodes.

server3 `/var/tmp`: 84316991488 available bytes; 95.29% used; 114152376 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106022993920 available bytes; 94.08% used; 114348273 free inodes.

server4 `/home`: 106022993920 available bytes; 94.08% used; 114348273 free inodes.

server4 `/data`: 116716838912 available bytes; 98.39% used; 224915576 free inodes.

server4 `/tmp`: 106022993920 available bytes; 94.08% used; 114348273 free inodes.

server4 `/var/tmp`: 106022993920 available bytes; 94.08% used; 114348273 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
