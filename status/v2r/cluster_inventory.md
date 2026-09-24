# V2R cluster inventory

2026-09-24T15:15:25.562403+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324045492224 available bytes; 81.92% used; 112481471 free inodes.

server1 `/home`: 324045492224 available bytes; 81.92% used; 112481471 free inodes.

server1 `/tmp`: 324045492224 available bytes; 81.92% used; 112481471 free inodes.

server1 `/var/tmp`: 324045492224 available bytes; 81.92% used; 112481471 free inodes.

server1 `/mnt/raid5`: 416797708288 available bytes; 98.09% used; 337662924 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57407090688 available bytes; 96.80% used; 110427655 free inodes.

server2 `/home`: 57407090688 available bytes; 96.80% used; 110427655 free inodes.

server2 `/tmp`: 57407090688 available bytes; 96.80% used; 110427655 free inodes.

server2 `/var/tmp`: 57407090688 available bytes; 96.80% used; 110427655 free inodes.

server2 `/mnt/raid5`: 503190781952 available bytes; 96.52% used; 445166581 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84853071872 available bytes; 95.26% used; 114182634 free inodes.

server3 `/home`: 84853071872 available bytes; 95.26% used; 114182634 free inodes.

server3 `/data`: 160487411712 available bytes; 97.78% used; 225807237 free inodes.

server3 `/tmp`: 84853071872 available bytes; 95.26% used; 114182634 free inodes.

server3 `/var/tmp`: 84853071872 available bytes; 95.26% used; 114182634 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716867072 available bytes; 94.10% used; 114348633 free inodes.

server4 `/home`: 105716867072 available bytes; 94.10% used; 114348633 free inodes.

server4 `/data`: 68783849472 available bytes; 99.05% used; 225256965 free inodes.

server4 `/tmp`: 105716867072 available bytes; 94.10% used; 114348633 free inodes.

server4 `/var/tmp`: 105716867072 available bytes; 94.10% used; 114348633 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
