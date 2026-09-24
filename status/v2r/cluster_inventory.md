# V2R cluster inventory

2026-09-24T08:50:19.616762+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324384440320 available bytes; 81.90% used; 112490261 free inodes.

server1 `/home`: 324384440320 available bytes; 81.90% used; 112490261 free inodes.

server1 `/tmp`: 324384440320 available bytes; 81.90% used; 112490261 free inodes.

server1 `/var/tmp`: 324384440320 available bytes; 81.90% used; 112490261 free inodes.

server1 `/mnt/raid5`: 504011141120 available bytes; 97.69% used; 337718107 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57797152768 available bytes; 96.78% used; 110430944 free inodes.

server2 `/home`: 57797152768 available bytes; 96.78% used; 110430944 free inodes.

server2 `/tmp`: 57797152768 available bytes; 96.78% used; 110430944 free inodes.

server2 `/var/tmp`: 57797152768 available bytes; 96.78% used; 110430944 free inodes.

server2 `/mnt/raid5`: 515526889472 available bytes; 96.44% used; 445179020 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85902163968 available bytes; 95.21% used; 114199578 free inodes.

server3 `/home`: 85902163968 available bytes; 95.21% used; 114199578 free inodes.

server3 `/data`: 168320659456 available bytes; 97.67% used; 225822076 free inodes.

server3 `/tmp`: 85902163968 available bytes; 95.21% used; 114199578 free inodes.

server3 `/var/tmp`: 85902163968 available bytes; 95.21% used; 114199578 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759682560 available bytes; 94.10% used; 114349073 free inodes.

server4 `/home`: 105759682560 available bytes; 94.10% used; 114349073 free inodes.

server4 `/data`: 319811887104 available bytes; 95.58% used; 225273501 free inodes.

server4 `/tmp`: 105759682560 available bytes; 94.10% used; 114349073 free inodes.

server4 `/var/tmp`: 105759682560 available bytes; 94.10% used; 114349073 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
