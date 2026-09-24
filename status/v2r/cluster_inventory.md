# V2R cluster inventory

2026-09-24T10:26:44.365389+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324412424192 available bytes; 81.90% used; 112489287 free inodes.

server1 `/home`: 324412424192 available bytes; 81.90% used; 112489287 free inodes.

server1 `/tmp`: 324412424192 available bytes; 81.90% used; 112489287 free inodes.

server1 `/var/tmp`: 324412424192 available bytes; 81.90% used; 112489287 free inodes.

server1 `/mnt/raid5`: 500169166848 available bytes; 97.71% used; 337698228 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57735913472 available bytes; 96.78% used; 110430673 free inodes.

server2 `/home`: 57735913472 available bytes; 96.78% used; 110430673 free inodes.

server2 `/tmp`: 57735913472 available bytes; 96.78% used; 110430673 free inodes.

server2 `/var/tmp`: 57735913472 available bytes; 96.78% used; 110430673 free inodes.

server2 `/mnt/raid5`: 512837611520 available bytes; 96.46% used; 445175557 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85554221056 available bytes; 95.23% used; 114189369 free inodes.

server3 `/home`: 85554221056 available bytes; 95.23% used; 114189369 free inodes.

server3 `/data`: 164335747072 available bytes; 97.73% used; 225818693 free inodes.

server3 `/tmp`: 85554221056 available bytes; 95.23% used; 114189369 free inodes.

server3 `/var/tmp`: 85554221056 available bytes; 95.23% used; 114189369 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744752640 available bytes; 94.10% used; 114348973 free inodes.

server4 `/home`: 105744752640 available bytes; 94.10% used; 114348973 free inodes.

server4 `/data`: 153472266240 available bytes; 97.88% used; 225258403 free inodes.

server4 `/tmp`: 105744752640 available bytes; 94.10% used; 114348973 free inodes.

server4 `/var/tmp`: 105744752640 available bytes; 94.10% used; 114348973 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
