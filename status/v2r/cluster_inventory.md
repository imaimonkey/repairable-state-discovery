# V2R cluster inventory

2026-09-24T05:32:38.735579+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324538691584 available bytes; 81.90% used; 112492330 free inodes.

server1 `/home`: 324538691584 available bytes; 81.90% used; 112492330 free inodes.

server1 `/tmp`: 324538691584 available bytes; 81.90% used; 112492330 free inodes.

server1 `/var/tmp`: 324538691584 available bytes; 81.90% used; 112492330 free inodes.

server1 `/mnt/raid5`: 517640892416 available bytes; 97.63% used; 337724198 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57917063168 available bytes; 96.77% used; 110431362 free inodes.

server2 `/home`: 57917063168 available bytes; 96.77% used; 110431362 free inodes.

server2 `/tmp`: 57917063168 available bytes; 96.77% used; 110431362 free inodes.

server2 `/var/tmp`: 57917063168 available bytes; 96.77% used; 110431362 free inodes.

server2 `/mnt/raid5`: 508559687680 available bytes; 96.49% used; 445193521 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127198588928 available bytes; 92.90% used; 114197408 free inodes.

server3 `/home`: 127198588928 available bytes; 92.90% used; 114197408 free inodes.

server3 `/data`: 185271218176 available bytes; 97.44% used; 225839537 free inodes.

server3 `/tmp`: 127198588928 available bytes; 92.90% used; 114197408 free inodes.

server3 `/var/tmp`: 127198588928 available bytes; 92.90% used; 114197408 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816932352 available bytes; 94.10% used; 114349363 free inodes.

server4 `/home`: 105816932352 available bytes; 94.10% used; 114349363 free inodes.

server4 `/data`: 251525844992 available bytes; 96.52% used; 225358108 free inodes.

server4 `/tmp`: 105816932352 available bytes; 94.10% used; 114349363 free inodes.

server4 `/var/tmp`: 105816932352 available bytes; 94.10% used; 114349363 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
