# V2R cluster inventory

2026-09-27T14:34:50.679358+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304741027840 available bytes; 83.00% used; 112401362 free inodes.

server1 `/home`: 304741027840 available bytes; 83.00% used; 112401362 free inodes.

server1 `/tmp`: 304741027840 available bytes; 83.00% used; 112401362 free inodes.

server1 `/var/tmp`: 304741027840 available bytes; 83.00% used; 112401362 free inodes.

server1 `/mnt/raid5`: 630116085760 available bytes; 97.11% used; 337424054 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13405564928 available bytes; 99.25% used; 110351782 free inodes.

server2 `/home`: 13405564928 available bytes; 99.25% used; 110351782 free inodes.

server2 `/tmp`: 13405564928 available bytes; 99.25% used; 110351782 free inodes.

server2 `/var/tmp`: 13405564928 available bytes; 99.25% used; 110351782 free inodes.

server2 `/mnt/raid5`: 526664601600 available bytes; 96.36% used; 444721948 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78557773824 available bytes; 95.62% used; 114062778 free inodes.

server3 `/home`: 78557773824 available bytes; 95.62% used; 114062778 free inodes.

server3 `/data`: 1328708521984 available bytes; 81.64% used; 225756782 free inodes.

server3 `/tmp`: 78557773824 available bytes; 95.62% used; 114062778 free inodes.

server3 `/var/tmp`: 78557773824 available bytes; 95.62% used; 114062778 free inodes.
| server4 | True | ['1', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109780000768 available bytes; 93.87% used; 114372756 free inodes.

server4 `/home`: 109780000768 available bytes; 93.87% used; 114372756 free inodes.

server4 `/data`: 350479568896 available bytes; 95.16% used; 224727370 free inodes.

server4 `/tmp`: 109780000768 available bytes; 93.87% used; 114372756 free inodes.

server4 `/var/tmp`: 109780000768 available bytes; 93.87% used; 114372756 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
