# V2R cluster inventory

2026-09-24T05:49:59.655140+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324527550464 available bytes; 81.90% used; 112492038 free inodes.

server1 `/home`: 324527550464 available bytes; 81.90% used; 112492038 free inodes.

server1 `/tmp`: 324527550464 available bytes; 81.90% used; 112492038 free inodes.

server1 `/var/tmp`: 324527550464 available bytes; 81.90% used; 112492038 free inodes.

server1 `/mnt/raid5`: 517614530560 available bytes; 97.63% used; 337723901 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57905778688 available bytes; 96.77% used; 110431318 free inodes.

server2 `/home`: 57905778688 available bytes; 96.77% used; 110431318 free inodes.

server2 `/tmp`: 57905778688 available bytes; 96.77% used; 110431318 free inodes.

server2 `/var/tmp`: 57905778688 available bytes; 96.77% used; 110431318 free inodes.

server2 `/mnt/raid5`: 521775255552 available bytes; 96.39% used; 445193519 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126807007232 available bytes; 92.92% used; 114175497 free inodes.

server3 `/home`: 126807007232 available bytes; 92.92% used; 114175497 free inodes.

server3 `/data`: 185219813376 available bytes; 97.44% used; 225838626 free inodes.

server3 `/tmp`: 126807007232 available bytes; 92.92% used; 114175497 free inodes.

server3 `/var/tmp`: 126807007232 available bytes; 92.92% used; 114175497 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815973888 available bytes; 94.10% used; 114349347 free inodes.

server4 `/home`: 105815973888 available bytes; 94.10% used; 114349347 free inodes.

server4 `/data`: 251480018944 available bytes; 96.52% used; 225357944 free inodes.

server4 `/tmp`: 105815973888 available bytes; 94.10% used; 114349347 free inodes.

server4 `/var/tmp`: 105815973888 available bytes; 94.10% used; 114349347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
