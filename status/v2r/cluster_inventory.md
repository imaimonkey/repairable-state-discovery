# V2R cluster inventory

2026-09-24T05:53:06.947767+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324527644672 available bytes; 81.90% used; 112492019 free inodes.

server1 `/home`: 324527644672 available bytes; 81.90% used; 112492019 free inodes.

server1 `/tmp`: 324527644672 available bytes; 81.90% used; 112492019 free inodes.

server1 `/var/tmp`: 324527644672 available bytes; 81.90% used; 112492019 free inodes.

server1 `/mnt/raid5`: 517608386560 available bytes; 97.63% used; 337723872 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57906151424 available bytes; 96.77% used; 110431312 free inodes.

server2 `/home`: 57906151424 available bytes; 96.77% used; 110431312 free inodes.

server2 `/tmp`: 57906151424 available bytes; 96.77% used; 110431312 free inodes.

server2 `/var/tmp`: 57906151424 available bytes; 96.77% used; 110431312 free inodes.

server2 `/mnt/raid5`: 521140322304 available bytes; 96.40% used; 445193292 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126806380544 available bytes; 92.92% used; 114175503 free inodes.

server3 `/home`: 126806380544 available bytes; 92.92% used; 114175503 free inodes.

server3 `/data`: 185874284544 available bytes; 97.43% used; 225838618 free inodes.

server3 `/tmp`: 126806380544 available bytes; 92.92% used; 114175503 free inodes.

server3 `/var/tmp`: 126806380544 available bytes; 92.92% used; 114175503 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815846912 available bytes; 94.10% used; 114349341 free inodes.

server4 `/home`: 105815846912 available bytes; 94.10% used; 114349341 free inodes.

server4 `/data`: 252144214016 available bytes; 96.52% used; 225357939 free inodes.

server4 `/tmp`: 105815846912 available bytes; 94.10% used; 114349341 free inodes.

server4 `/var/tmp`: 105815846912 available bytes; 94.10% used; 114349341 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
