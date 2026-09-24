# V2R cluster inventory

2026-09-24T09:18:17.710249+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324466642944 available bytes; 81.90% used; 112489962 free inodes.

server1 `/home`: 324466642944 available bytes; 81.90% used; 112489962 free inodes.

server1 `/tmp`: 324466642944 available bytes; 81.90% used; 112489962 free inodes.

server1 `/var/tmp`: 324466642944 available bytes; 81.90% used; 112489962 free inodes.

server1 `/mnt/raid5`: 503204675584 available bytes; 97.69% used; 337714762 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57777606656 available bytes; 96.78% used; 110430850 free inodes.

server2 `/home`: 57777606656 available bytes; 96.78% used; 110430850 free inodes.

server2 `/tmp`: 57777606656 available bytes; 96.78% used; 110430850 free inodes.

server2 `/var/tmp`: 57777606656 available bytes; 96.78% used; 110430850 free inodes.

server2 `/mnt/raid5`: 514974683136 available bytes; 96.44% used; 445178173 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85881073664 available bytes; 95.21% used; 114199170 free inodes.

server3 `/home`: 85881073664 available bytes; 95.21% used; 114199170 free inodes.

server3 `/data`: 165883744256 available bytes; 97.71% used; 225821129 free inodes.

server3 `/tmp`: 85881073664 available bytes; 95.21% used; 114199170 free inodes.

server3 `/var/tmp`: 85881073664 available bytes; 95.21% used; 114199170 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758203904 available bytes; 94.10% used; 114349053 free inodes.

server4 `/home`: 105758203904 available bytes; 94.10% used; 114349053 free inodes.

server4 `/data`: 302824329216 available bytes; 95.81% used; 225273342 free inodes.

server4 `/tmp`: 105758203904 available bytes; 94.10% used; 114349053 free inodes.

server4 `/var/tmp`: 105758203904 available bytes; 94.10% used; 114349053 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
