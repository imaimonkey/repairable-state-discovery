# V2R cluster inventory

2026-09-25T08:17:37.907855+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318828363776 available bytes; 82.21% used; 112480352 free inodes.

server1 `/home`: 318828363776 available bytes; 82.21% used; 112480352 free inodes.

server1 `/tmp`: 318828363776 available bytes; 82.21% used; 112480352 free inodes.

server1 `/var/tmp`: 318828363776 available bytes; 82.21% used; 112480352 free inodes.

server1 `/mnt/raid5`: 379082186752 available bytes; 98.26% used; 337557498 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22834896896 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22834896896 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22834896896 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22834896896 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 333669203968 available bytes; 97.69% used; 445094971 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84439494656 available bytes; 95.29% used; 114156055 free inodes.

server3 `/home`: 84439494656 available bytes; 95.29% used; 114156055 free inodes.

server3 `/data`: 142386896896 available bytes; 98.03% used; 225811893 free inodes.

server3 `/tmp`: 84439494656 available bytes; 95.29% used; 114156055 free inodes.

server3 `/var/tmp`: 84439494656 available bytes; 95.29% used; 114156055 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625014272 available bytes; 94.11% used; 114350334 free inodes.

server4 `/home`: 105625014272 available bytes; 94.11% used; 114350334 free inodes.

server4 `/data`: 248484200448 available bytes; 96.57% used; 225006965 free inodes.

server4 `/tmp`: 105625014272 available bytes; 94.11% used; 114350334 free inodes.

server4 `/var/tmp`: 105625014272 available bytes; 94.11% used; 114350334 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
