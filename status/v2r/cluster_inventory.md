# V2R cluster inventory

2026-09-24T05:40:31.773313+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324530438144 available bytes; 81.90% used; 112492160 free inodes.

server1 `/home`: 324530438144 available bytes; 81.90% used; 112492160 free inodes.

server1 `/tmp`: 324530438144 available bytes; 81.90% used; 112492160 free inodes.

server1 `/var/tmp`: 324530438144 available bytes; 81.90% used; 112492160 free inodes.

server1 `/mnt/raid5`: 517628911616 available bytes; 97.63% used; 337723947 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57916088320 available bytes; 96.77% used; 110431344 free inodes.

server2 `/home`: 57916088320 available bytes; 96.77% used; 110431344 free inodes.

server2 `/tmp`: 57916088320 available bytes; 96.77% used; 110431344 free inodes.

server2 `/var/tmp`: 57916088320 available bytes; 96.77% used; 110431344 free inodes.

server2 `/mnt/raid5`: 522058383360 available bytes; 96.39% used; 445193616 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126796746752 available bytes; 92.92% used; 114174191 free inodes.

server3 `/home`: 126796746752 available bytes; 92.92% used; 114174191 free inodes.

server3 `/data`: 185250054144 available bytes; 97.44% used; 225839174 free inodes.

server3 `/tmp`: 126796746752 available bytes; 92.92% used; 114174191 free inodes.

server3 `/var/tmp`: 126796746752 available bytes; 92.92% used; 114174191 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816424448 available bytes; 94.10% used; 114349353 free inodes.

server4 `/home`: 105816424448 available bytes; 94.10% used; 114349353 free inodes.

server4 `/data`: 251477241856 available bytes; 96.52% used; 225358021 free inodes.

server4 `/tmp`: 105816424448 available bytes; 94.10% used; 114349353 free inodes.

server4 `/var/tmp`: 105816424448 available bytes; 94.10% used; 114349353 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
