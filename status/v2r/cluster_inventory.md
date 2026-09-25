# V2R cluster inventory

2026-09-25T05:13:02.587701+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318894080000 available bytes; 82.21% used; 112480308 free inodes.

server1 `/home`: 318894080000 available bytes; 82.21% used; 112480308 free inodes.

server1 `/tmp`: 318894080000 available bytes; 82.21% used; 112480308 free inodes.

server1 `/var/tmp`: 318894080000 available bytes; 82.21% used; 112480308 free inodes.

server1 `/mnt/raid5`: 408585854976 available bytes; 98.13% used; 337570426 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929965056 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22929965056 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22929965056 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22929965056 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461184860160 available bytes; 96.81% used; 445108872 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339093504 available bytes; 95.29% used; 114156067 free inodes.

server3 `/home`: 84339093504 available bytes; 95.29% used; 114156067 free inodes.

server3 `/data`: 142791139328 available bytes; 98.03% used; 225815250 free inodes.

server3 `/tmp`: 84339093504 available bytes; 95.29% used; 114156067 free inodes.

server3 `/var/tmp`: 84339093504 available bytes; 95.29% used; 114156067 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658982400 available bytes; 94.10% used; 114350409 free inodes.

server4 `/home`: 105658982400 available bytes; 94.10% used; 114350409 free inodes.

server4 `/data`: 26323353600 available bytes; 99.64% used; 224960459 free inodes.

server4 `/tmp`: 105658982400 available bytes; 94.10% used; 114350409 free inodes.

server4 `/var/tmp`: 105658982400 available bytes; 94.10% used; 114350409 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
