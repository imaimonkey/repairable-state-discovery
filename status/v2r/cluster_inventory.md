# V2R cluster inventory

2026-09-25T14:58:24.298515+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319139262464 available bytes; 82.20% used; 112476943 free inodes.

server1 `/home`: 319139262464 available bytes; 82.20% used; 112476943 free inodes.

server1 `/tmp`: 319139262464 available bytes; 82.20% used; 112476943 free inodes.

server1 `/var/tmp`: 319139262464 available bytes; 82.20% used; 112476943 free inodes.

server1 `/mnt/raid5`: 371114463232 available bytes; 98.30% used; 337546428 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 14378811392 available bytes; 99.20% used; 110407653 free inodes.

server2 `/home`: 14378811392 available bytes; 99.20% used; 110407653 free inodes.

server2 `/tmp`: 14378811392 available bytes; 99.20% used; 110407653 free inodes.

server2 `/var/tmp`: 14378811392 available bytes; 99.20% used; 110407653 free inodes.

server2 `/mnt/raid5`: 320889671680 available bytes; 97.78% used; 445073948 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84349034496 available bytes; 95.29% used; 114153954 free inodes.

server3 `/home`: 84349034496 available bytes; 95.29% used; 114153954 free inodes.

server3 `/data`: 142187814912 available bytes; 98.03% used; 225808224 free inodes.

server3 `/tmp`: 84349034496 available bytes; 95.29% used; 114153954 free inodes.

server3 `/var/tmp`: 84349034496 available bytes; 95.29% used; 114153954 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105636757504 available bytes; 94.11% used; 114349709 free inodes.

server4 `/home`: 105636757504 available bytes; 94.11% used; 114349709 free inodes.

server4 `/data`: 231416557568 available bytes; 96.80% used; 224945157 free inodes.

server4 `/tmp`: 105636757504 available bytes; 94.11% used; 114349709 free inodes.

server4 `/var/tmp`: 105636757504 available bytes; 94.11% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
