# V2R cluster inventory

2026-09-24T09:16:50.021692+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324467884032 available bytes; 81.90% used; 112489971 free inodes.

server1 `/home`: 324467884032 available bytes; 81.90% used; 112489971 free inodes.

server1 `/tmp`: 324467884032 available bytes; 81.90% used; 112489971 free inodes.

server1 `/var/tmp`: 324467884032 available bytes; 81.90% used; 112489971 free inodes.

server1 `/mnt/raid5`: 503204466688 available bytes; 97.69% used; 337714937 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57776660480 available bytes; 96.78% used; 110430929 free inodes.

server2 `/home`: 57776660480 available bytes; 96.78% used; 110430929 free inodes.

server2 `/tmp`: 57776660480 available bytes; 96.78% used; 110430929 free inodes.

server2 `/var/tmp`: 57776660480 available bytes; 96.78% used; 110430929 free inodes.

server2 `/mnt/raid5`: 514465529856 available bytes; 96.45% used; 445177887 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85881077760 available bytes; 95.21% used; 114199167 free inodes.

server3 `/home`: 85881077760 available bytes; 95.21% used; 114199167 free inodes.

server3 `/data`: 165896028160 available bytes; 97.71% used; 225821151 free inodes.

server3 `/tmp`: 85881077760 available bytes; 95.21% used; 114199167 free inodes.

server3 `/var/tmp`: 85881077760 available bytes; 95.21% used; 114199167 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758253056 available bytes; 94.10% used; 114349052 free inodes.

server4 `/home`: 105758253056 available bytes; 94.10% used; 114349052 free inodes.

server4 `/data`: 302821076992 available bytes; 95.81% used; 225273340 free inodes.

server4 `/tmp`: 105758253056 available bytes; 94.10% used; 114349052 free inodes.

server4 `/var/tmp`: 105758253056 available bytes; 94.10% used; 114349052 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
