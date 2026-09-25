# V2R cluster inventory

2026-09-25T11:51:50.109355+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319047356416 available bytes; 82.20% used; 112478823 free inodes.

server1 `/home`: 319047356416 available bytes; 82.20% used; 112478823 free inodes.

server1 `/tmp`: 319047356416 available bytes; 82.20% used; 112478823 free inodes.

server1 `/var/tmp`: 319047356416 available bytes; 82.20% used; 112478823 free inodes.

server1 `/mnt/raid5`: 365341310976 available bytes; 98.32% used; 337549161 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22905536512 available bytes; 98.72% used; 110409974 free inodes.

server2 `/home`: 22905536512 available bytes; 98.72% used; 110409974 free inodes.

server2 `/tmp`: 22905536512 available bytes; 98.72% used; 110409974 free inodes.

server2 `/var/tmp`: 22905536512 available bytes; 98.72% used; 110409974 free inodes.

server2 `/mnt/raid5`: 326011613184 available bytes; 97.75% used; 445082162 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84213993472 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84213993472 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142040637440 available bytes; 98.04% used; 225813304 free inodes.

server3 `/tmp`: 84213993472 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84213993472 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105602428928 available bytes; 94.11% used; 114350231 free inodes.

server4 `/home`: 105602428928 available bytes; 94.11% used; 114350231 free inodes.

server4 `/data`: 232568705024 available bytes; 96.79% used; 224974284 free inodes.

server4 `/tmp`: 105602428928 available bytes; 94.11% used; 114350231 free inodes.

server4 `/var/tmp`: 105602428928 available bytes; 94.11% used; 114350231 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
