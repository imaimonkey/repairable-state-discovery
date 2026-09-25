# V2R cluster inventory

2026-09-25T18:12:44.711270+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318761717760 available bytes; 82.22% used; 112476350 free inodes.

server1 `/home`: 318761717760 available bytes; 82.22% used; 112476350 free inodes.

server1 `/tmp`: 318761717760 available bytes; 82.22% used; 112476350 free inodes.

server1 `/var/tmp`: 318761717760 available bytes; 82.22% used; 112476350 free inodes.

server1 `/mnt/raid5`: 371215896576 available bytes; 98.30% used; 337542216 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23098073088 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23098073088 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23098073088 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23098073088 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 314490875904 available bytes; 97.83% used; 445067153 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84392222720 available bytes; 95.29% used; 114152617 free inodes.

server3 `/home`: 84392222720 available bytes; 95.29% used; 114152617 free inodes.

server3 `/data`: 131471695872 available bytes; 98.18% used; 225810208 free inodes.

server3 `/tmp`: 84392222720 available bytes; 95.29% used; 114152617 free inodes.

server3 `/var/tmp`: 84392222720 available bytes; 95.29% used; 114152617 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616330752 available bytes; 94.11% used; 114349603 free inodes.

server4 `/home`: 105616330752 available bytes; 94.11% used; 114349603 free inodes.

server4 `/data`: 229726429184 available bytes; 96.83% used; 224932217 free inodes.

server4 `/tmp`: 105616330752 available bytes; 94.11% used; 114349603 free inodes.

server4 `/var/tmp`: 105616330752 available bytes; 94.11% used; 114349603 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
