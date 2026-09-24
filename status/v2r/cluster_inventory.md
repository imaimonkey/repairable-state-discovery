# V2R cluster inventory

2026-09-24T02:53:18.671661+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325382565888 available bytes; 81.85% used; 112498664 free inodes.

server1 `/home`: 325382565888 available bytes; 81.85% used; 112498664 free inodes.

server1 `/tmp`: 325382565888 available bytes; 81.85% used; 112498664 free inodes.

server1 `/var/tmp`: 325382565888 available bytes; 81.85% used; 112498664 free inodes.

server1 `/mnt/raid5`: 548545552384 available bytes; 97.48% used; 337732359 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40872656896 available bytes; 97.72% used; 110431372 free inodes.

server2 `/home`: 40872656896 available bytes; 97.72% used; 110431372 free inodes.

server2 `/tmp`: 40872656896 available bytes; 97.72% used; 110431372 free inodes.

server2 `/var/tmp`: 40872656896 available bytes; 97.72% used; 110431372 free inodes.

server2 `/mnt/raid5`: 528307245056 available bytes; 96.35% used; 445199057 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292288323584 available bytes; 83.69% used; 114186965 free inodes.

server3 `/home`: 292288323584 available bytes; 83.69% used; 114186965 free inodes.

server3 `/data`: 39728283648 available bytes; 99.45% used; 225845839 free inodes.

server3 `/tmp`: 292288323584 available bytes; 83.69% used; 114186965 free inodes.

server3 `/var/tmp`: 292288323584 available bytes; 83.69% used; 114186965 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002579456 available bytes; 94.08% used; 114349808 free inodes.

server4 `/home`: 106002579456 available bytes; 94.08% used; 114349808 free inodes.

server4 `/data`: 289728917504 available bytes; 96.00% used; 225386951 free inodes.

server4 `/tmp`: 106002579456 available bytes; 94.08% used; 114349808 free inodes.

server4 `/var/tmp`: 106002579456 available bytes; 94.08% used; 114349808 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
