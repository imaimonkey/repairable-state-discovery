# V2R cluster inventory

2026-09-25T06:37:53.268437+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872887296 available bytes; 82.21% used; 112480357 free inodes.

server1 `/home`: 318872887296 available bytes; 82.21% used; 112480357 free inodes.

server1 `/tmp`: 318872887296 available bytes; 82.21% used; 112480357 free inodes.

server1 `/var/tmp`: 318872887296 available bytes; 82.21% used; 112480357 free inodes.

server1 `/mnt/raid5`: 399799832576 available bytes; 98.17% used; 337561399 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22886969344 available bytes; 98.72% used; 110410526 free inodes.

server2 `/home`: 22886969344 available bytes; 98.72% used; 110410526 free inodes.

server2 `/tmp`: 22886969344 available bytes; 98.72% used; 110410526 free inodes.

server2 `/var/tmp`: 22886969344 available bytes; 98.72% used; 110410526 free inodes.

server2 `/mnt/raid5`: 370325745664 available bytes; 97.44% used; 445099548 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84450562048 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84450562048 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142532599808 available bytes; 98.03% used; 225813668 free inodes.

server3 `/tmp`: 84450562048 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84450562048 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639563264 available bytes; 94.10% used; 114350385 free inodes.

server4 `/home`: 105639563264 available bytes; 94.10% used; 114350385 free inodes.

server4 `/data`: 251136589824 available bytes; 96.53% used; 225019361 free inodes.

server4 `/tmp`: 105639563264 available bytes; 94.10% used; 114350385 free inodes.

server4 `/var/tmp`: 105639563264 available bytes; 94.10% used; 114350385 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
